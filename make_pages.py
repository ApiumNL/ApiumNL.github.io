from jinja2 import Environment, FileSystemLoader, select_autoescape

import config


def main():
    env = Environment(loader=FileSystemLoader('templates'),
                      autoescape=select_autoescape(['html', 'xml']))

    tpl_vars = {name: getattr(config, name) for name in dir(config)
                if not name.startswith("__")}

    for tpl_name in env.list_templates():
        tpl = env.get_template(tpl_name)

        with open(f"dist/{tpl_name}", "w") as fh:
            fh.write(tpl.render(**tpl_vars))


if __name__ == "__main__":
    main()
