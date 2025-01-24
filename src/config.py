from dataclasses import dataclass, asdict

# Configuração geral do jogo
@dataclass
class GameConfig:
    screen_width: int = 500
    screen_height: int = 800
    fps: int = 30
    
    def to_dict(self):
        """Converte as configurações em um dicionário."""
        return asdict(self)

# Configuração da fonte
@dataclass
class FontConfig:
    style: str = "arial"
    size: int = 50

    def to_dict(self):
        """Converte as configurações em um dicionário."""
        return asdict(self)

# Configuração do pássaro
@dataclass
class BirdConfig:
    # transform_size: int = 2
    rotation_max: int = 30  # Antes: 25
    rotation_min: int = -70  # Antes: 25
    rotation_speed: int = 7  # Antes: 20
    animation_duration: int = 5
    jump_speed: float = -10.5  # Deve ser negativo
    acceleration: float = 1.5
    position_x: int = 230
    position_y: int = 350
    
    def to_dict(self):
        """Converte as configurações em um dicionário."""
        return asdict(self)

# Configuração dos canos
@dataclass
class PipeConfig:
    x_distance: int = 600
    y_distance: int = 400  # Antes: 200
    speed: int = 5
    height_max: int = 50
    height_min: int = 450
    
    def to_dict(self):
        """Converte as configurações em um dicionário."""
        return asdict(self)

# Configuração da base
@dataclass
class BaseConfig:
    speed: int = 5
    position_y: int = 730
    
    def to_dict(self):
        """Converte as configurações em um dicionário."""
        return asdict(self)

# Instâncias das configurações
# game_config = GameConfig()
# font_config = FontConfig()
# bird_config = BirdConfig()
# pipe_config = PipeConfig()
# base_config = BaseConfig()
