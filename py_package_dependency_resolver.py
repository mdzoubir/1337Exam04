def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    res = []
    while len(res) < len(packages):
        ready = []
        for pkg in packages:
            if pkg in res:
                continue  # already installed

            can_install = True
            for dep in packages[pkg]:
                if dep not in res:
                    can_install = False  # real dependency not installed yet

            if can_install:
                ready.append(pkg)

        if not ready:
            return []  # stuck: circular dependency
        res += sorted(ready)
    return res

print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))  # Expected: ["driver", "database", "app"]
print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))  # Expected: ["A", "B", "C"]
print(package_dependency_resolver({}))  # Expected: []
print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))  # Expected: []
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))  # Expected: ["api", "web", "backend", "frontend"]
