#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""
import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación optimizada para la campaña 'La hora del Bon Yurt'.
    """
    
    def classify_topic(comment: str) -> str:
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Momentos o Deseos de Consumo
        # Captura antojo, momentos del día (noche, tarde) y deseos inmediatos.
        if re.search(
            r'ganas|antojo|quiero|necesito|ya\b|noche|tarde|mañana|'
            r'hambre|comprar|delicia|antojada|antojado|d[oó]nde lo consigo',
            comment_lower
        ):
            return 'Momentos o deseos de consumo'
        
        # CATEGORÍA 2: Ingredientes / Salud
        # Específicamente para temas nutricionales, azúcar y componentes.
        if re.search(
            r'az[uú]car|dulce|calor[ií]as|grasa|nutrici[oó]n|salud|'
            r'qu[ií]micos|ingredientes|fitness|dieta',
            comment_lower
        ):
            return 'Ingredientes / Salud'
        
        # CATEGORÍA 3: Reacción a Creatividades y Humor
        # Para comentarios sobre el estilo del video, la gracia o comparaciones con otros anuncios.
        if re.search(
            r'anuncio|comercial|publicidad|gracia|chiste|risa|jsjs|jaja|'
            r'aguila|cerveza|parece|video|contenido|humor|peccao|ladra',
            comment_lower
        ):
            return 'Reacción a Creatividades / Humor'
            
        # CATEGORÍA 4: Opinión General del Producto / Sabor
        # Feedback directo sobre si les gusta el Bon Yurt en sí.
        if re.search(
            r'rico|delicioso|bueno|malo|feo|mejor|favorito|encanta|gusta',
            comment_lower
        ):
            return 'Opinión General del Producto'
        
        # CATEGORÍA 5: Interacciones Cortas / Religiosas / No Relevantes
        # Limpieza de "Amén", spam o comentarios de 1-2 palabras sin contexto.
        if re.search(
            r'am[eé]n|bendiciones|gracias|🙏🏼|🙌',
            comment_lower
        ) or len(comment_lower.split()) < 3:
            return 'Fuera de Tema / No Relevante'
        
        # CATEGORÍA DEFAULT
        return 'Otros'
    
    return classify_topic

# Ejemplo de prueba con tus comentarios:
classifier = create_topic_classifier()
print(classifier("que ganas de uno yaaaaa (son las 12 de la noche)")) # -> Momentos o deseos de consumo
print(classifier("Mera azucar")) # -> Ingredientes / Salud
print(classifier("Parece un anuncio de aguila jsjsjsjs")) # -> Reacción a Creatividades / Humor
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
