"""Build the React SPA and copy it to Vercel's static public directory."""

from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parent.parent
FRONTEND = ROOT / "frontend"
DIST = FRONTEND / "dist"
PUBLIC = ROOT / "public"


def main() -> None:
    subprocess.run(["npm", "ci"], cwd=FRONTEND, check=True)
    subprocess.run(["npm", "run", "build"], cwd=FRONTEND, check=True)
    if not (DIST / "index.html").is_file():
        raise SystemExit("Vite build did not produce frontend/dist/index.html")
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)
    for source in DIST.iterdir():
        # The homepage must pass through Flask so it can mint the auth cookies.
        if source.name == "index.html":
            continue
        target = PUBLIC / source.name
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)
    print(f"Copied {DIST} to {PUBLIC}")


if __name__ == "__main__":
    main()
