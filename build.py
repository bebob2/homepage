import os
import shutil
from staticjinja import Site

def build_site():
    # 1. Verzeichnisse definieren
    src = "templates"
    out = "docs"
    static_src = "static"
    static_dest = os.path.join(out, "static")

    # 2. Site konfigurieren und HTML rendern
    site = Site.make_site(searchpath=src, outpath=out)
    site.render()
    print(f"✅ HTML-Templates aus '{src}' nach '{out}' gerendert.")

    # 3. Statische Dateien manuell kopieren
    if os.path.exists(static_src):
        if os.path.exists(static_dest):
            shutil.rmtree(static_dest) # Alten Ordner löschen
        shutil.copytree(static_src, static_dest)
        print(f"✅ Statische Dateien aus '{static_src}' nach '{static_dest}' kopiert.")
    else:
        print(f"⚠️ Warnung: Ordner '{static_src}' nicht gefunden!")

if __name__ == "__main__":
    build_site()
