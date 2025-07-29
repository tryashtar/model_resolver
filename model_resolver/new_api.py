from typing import Any
from beet import ResourcePack
from PIL.Image import Image
from dataclasses import dataclass

from model_resolver.item_model.model import ItemModelBase, TintSource
from model_resolver.minecraft_model import MinecraftModel
from model_resolver.tasks.structure import BlockState, StructureDataModel

@dataclass
class RenderSettings:
   pack: ResourcePack
   size: int

def render_item(item: str, count: int, components: dict[str, Any], settings: RenderSettings) -> Image:
   pass

def render_block(block: str, states: dict[str, Any], settings: RenderSettings) -> Image:
   pass

def render_blockstate(state: BlockState, states: dict[str, Any], settings: RenderSettings):
   pass

def render_item_model(model: ItemModelBase, settings: RenderSettings) -> Image:
   pass

def render_model(model: MinecraftModel, settings: RenderSettings) -> Image:
   pass

def render_structure(structure: StructureDataModel, settings: RenderSettings) -> Image:
   pass
