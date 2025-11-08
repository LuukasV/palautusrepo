class Project:
    def __init__(self, name, description, lisenssi, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.lisenssi = lisenssi

        self.authors = authors

        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        author_string = ""
        for author in self.authors:
            author_string.join(f"\n- {author}")

        dependency_string = ""
        for dependency in self.dependencies:
            dependency_string.join(f"\n- {dependency}")

        dev_dependency_string = ""
        for dependency in self.dev_dependencies:
            dev_dependency_string.join(f"\n- {dependency}")

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.lisenssi or '-'}"
            "\n"
            "\nAuthors:"
            f"{author_string}"
            "\n"
            "\nDependencies:"
            f"{dependency_string}"
            "\n"
            f"\nDevelopment dependencies:"
            f"{dev_dependency_string}"
        )
