colors = []
brands = []

with open('color_brand/colors.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        words = line.split(' ')
        color = ""
        for word in words:
            word = word.strip()
            word = word[0].upper() + word[1:].lower()
            color += word + " "
        colors.append(color)

with open('color_brand/brands.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        words = line.split(' ')
        brand = ""
        for word in words:
            word = word.strip()
            word = word[0].upper() + word[1:].lower()
            brand += word + " "
        brands.append(brand)
