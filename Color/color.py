def calculate_related_colors(hex_color):
    """
    """
    hex_color = hex_color.lstrip("#")

    # 将 HEX 转换为 RGB 值
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    # 计算 HSV 值
    mx = max(r, g, b)
    mn = min(r, g, b)

    df = mx - mn

    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    else:
        h = 0

    s = 0 if mx == 0 else df / mx * 100
    v = mx / 255 * 100

    return h, s, v
