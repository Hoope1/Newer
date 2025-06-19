# tile_utils.py – Teil 3/4

import torch
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def split_into_tiles(img_tensor, tile_size=512, overlap=32):
    b, c, h, w = img_tensor.shape
    tiles = []
    positions = []

    stride = tile_size - overlap
    for y in range(0, h, stride):
        for x in range(0, w, stride):
            x_end = min(x + tile_size, w)
            y_end = min(y + tile_size, h)
            x_start = max(x_end - tile_size, 0)
            y_start = max(y_end - tile_size, 0)

            tile = img_tensor[:, :, y_start:y_start + tile_size, x_start:x_start + tile_size]
            tiles.append(tile)
            positions.append((x_start, y_start))

    return tiles, positions, h, w

def stitch_tiles(tiles, positions, full_height, full_width, tile_size=512, overlap=32):
    # Ergebnis-Vorbereitung
    out_tensor = torch.zeros(1, 1, full_height, full_width, device=device)
    weight_mask = torch.zeros_like(out_tensor)

    # Fensterfunktion (weicher Übergang)
    window = torch.ones(1, 1, tile_size, tile_size, device=device)
    if overlap > 0:
        fade = torch.linspace(0.0, 1.0, steps=overlap, device=device)
        window[:, :, :overlap, :] *= fade.view(-1, 1)
        window[:, :, -overlap:, :] *= fade.flip(0).view(-1, 1)
        window[:, :, :, :overlap] *= fade.view(1, -1)
        window[:, :, :, -overlap:] *= fade.flip(0).view(1, -1)

    # Zusammenfügen
    for tile_out, (x, y) in zip(tiles, positions):
        out_tensor[:, :, y:y+tile_size, x:x+tile_size] += tile_out * window
        weight_mask[:, :, y:y+tile_size, x:x+tile_size] += window

    # Division durch Gewicht
    weight_mask[weight_mask == 0] = 1.0
    result = out_tensor / weight_mask
    return result

def process_with_dexined_tiles(img_tensor, model, tile_size=512, overlap=32):
    model.eval()
    tiles, positions, h, w = split_into_tiles(img_tensor, tile_size, overlap)
    edge_tiles = []

    with torch.no_grad():
        for tile in tiles:
            output = model(tile.to(device))[-1]
            edge_tiles.append(output)

    stitched = stitch_tiles(edge_tiles, positions, h, w, tile_size, overlap)
    return stitched
