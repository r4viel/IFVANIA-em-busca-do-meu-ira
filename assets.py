import os
import pygame

BASE_DIR = os.path.dirname(
          os.path.abspath(__file__)
          )
IMAGE_DIR = os.path.join(
    BASE_DIR,"assets","images"
)

_cache={}
_warning=set()

def _placeholder(size,color=(255,0,255)):
    surf = pygame.Surface(size,pygame.SRCALPHA)
    surf.fill(color,180)
    pygame.draw.rect(surf,(255,255,255)
                     ,surf.get_rect(),2)
    return surf

def load_image(path, size=None,
               fallback_color=(255,0,255)):
    chave = (path,size)
    if chave in _cache:
        return _cache[chave]
    caminho = os.path.join(IMAGE_DIR,path)
    if not os.path.isfile(caminho):
        if caminho not in _warning:
            _warning.add(caminho)
        image = _placeholder(size or (32,32),
                             fallback_color)
    else:
        image = pygame.image.load(
                caminho).convert_alpha()
        if size is not None and (
            image.get_size() != size):
            image = pygame.transform.smoothscale(
                image,size
            )
    _cache[chave]=image
    return image

def virar_imagem(path,size=None,
                 fallback_color=(255,0,255)):
    chave = (path,chave,"virada")
    if chave in _cache:
        return _cache[chave]
    base = load_image(path,size,fallback_color)
    virar = pygame.transform.flip(base,True,False)
    _cache[chave] = virar
    return virar

def clear_cache():
    _cache.clear()
