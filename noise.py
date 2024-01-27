import random
def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
    return a + t * (b - a)

def gradient(h, x, y):
    gradients = [[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]]
    gradient = gradients[int(h) % 8]
    return gradient[0] * x + gradient[1] * y

def perlin(x, y, random_shift_x, random_shift_y):
    random_shift_x = random_shift_x = random.randint(-25,25)+random_shift_x
    random_shift_y = random_shift_y = random.randint(-25,25)+random_shift_y
    
    X = int(x + random_shift_x) & 255
    Y = int(y + random_shift_y) & 255
    
    xf = x - int(x)
    yf = y - int(y)
    
    u = fade(xf)
    v = fade(yf)
    
    p = [0] * 512  # Ensure that p has sufficient length
    for i in range(256):
        p[i] = p[i + 256] = i
    
    p[0] = p[0] + gradient(p[X]+Y, xf, yf)
    p[1] = p[1] + gradient(p[X+1]+Y, xf-1, yf)
    p[2] = p[2] + gradient(p[X]+Y+1, xf, yf-1)
    p[3] = p[3] + gradient(p[X+1]+Y+1, xf-1, yf-1)
    
    return lerp(lerp(p[0], p[1], u), lerp(p[2], p[3], u), v)
