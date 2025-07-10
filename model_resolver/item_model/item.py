from pydantic import BaseModel, Field
from typing import Any, Self
from beet import Context
from beet.contrib.vanilla import Release
from model_resolver.utils import get_default_components, resolve_key


class Item(BaseModel):
    id: str
    count: int = 1
    components_from_user: dict[str, Any] = Field(
        default_factory=dict, alias="components"
    )
    default_components: dict[str, Any] = Field(default_factory=dict)

    __resolved__: bool = False

    def fill(self, ctx: Context, release: Release) -> Self:
        if self.__resolved__:
            return self
        components = get_default_components(ctx, release)
        real_id = resolve_key(self.id)
        if real_id in components:
            self.default_components = components[real_id]
        self.__resolved__ = True
        return self

    @property
    def components(self) -> dict[str, Any]:
        return {**self.default_components, **self.components_from_user}

    def get(self, component_name: str) -> Any:
        key = resolve_key(component_name)
        namespace, path = key.split(":", 1)
        return self.components.get(key, self.components.get(path, None))
