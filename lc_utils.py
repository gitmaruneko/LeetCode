"""
Shared utilities for LeetCode solution files.
"""


def analyze_complexity(method):
    """Heuristic AST-based complexity analyzer for a solve() method.

    Returns (time_complexity, space_complexity) as strings, e.g. ("O(n)", "O(1)").
    """
    import ast
    import inspect
    import textwrap

    try:
        src = textwrap.dedent(inspect.getsource(method))
        tree = ast.parse(src)
    except Exception:
        return "O(?)", "O(?)"

    # --- Time complexity: estimate from max loop-nesting depth ---
    def _max_loop_depth(node, depth=0):
        if isinstance(node, (ast.For, ast.While)):
            depth += 1
        child_depths = [_max_loop_depth(c, depth) for c in ast.iter_child_nodes(node)]
        return max(child_depths) if child_depths else depth

    depth = _max_loop_depth(tree)
    has_log = any(p in src for p in ("//= 2", ">>= 1", "// 2", "math.log", "bisect"))

    if depth == 0:
        time_c = "O(1)"
    elif depth == 1:
        time_c = "O(n log n)" if has_log else "O(n)"
    elif depth == 2:
        time_c = "O(n^2)"
    else:
        time_c = "O(n^%d)" % depth

    # --- Space complexity: detect heap allocations ---
    class _SpaceChecker(ast.NodeVisitor):
        found = False

        def visit_List(self, node):
            self.found = True
            self.generic_visit(node)

        def visit_Dict(self, node):
            self.found = True
            self.generic_visit(node)

        def visit_Set(self, node):
            self.found = True
            self.generic_visit(node)

        def visit_Call(self, node):
            heap_types = ("list", "dict", "set", "defaultdict", "Counter", "deque")
            if isinstance(node.func, ast.Name) and node.func.id in heap_types:
                self.found = True
            self.generic_visit(node)

    checker = _SpaceChecker()
    checker.visit(tree)
    space_c = "O(n)" if checker.found else "O(1)"

    return time_c, space_c
