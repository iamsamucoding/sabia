from .dash_engine import DashEngine

class EngineFactory:
    @staticmethod
    def create_engine(engine_type: str) -> 'RenderEngine':
        engine_type_lw = engine_type.lower()

        engines = {
            'dash': DashEngine()
        }

        render_engine = engines.get(engine_type)

        if render_engine is None:
            raise ValueError(f"Unknown engine type: {engine_type}")
        
        return render_engine