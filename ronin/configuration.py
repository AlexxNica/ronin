
from .utils.paths import build_path, base_path
import inspect, sys

def configure_build(ctx, root_path=None, output_path_relative='build', binary_path_relative='bin', object_path_relative='obj', debug=True, frame=1):
    ctx.input_path = root_path or base_path(inspect.getfile(sys._getframe(frame)))
    ctx.output_path = build_path(root_path, output_path_relative)
    ctx.binary_path_relative = binary_path_relative
    ctx.object_path_relative = object_path_relative
    ctx.debug = debug