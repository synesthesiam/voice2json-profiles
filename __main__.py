"""Github-like download interface"""
import typing
from pathlib import Path
from uuid import uuid4

from quart import Quart, send_from_directory, Response

app = Quart("rhasspy")
app.secret_key = str(uuid4())

# -----------------------------------------------------------------------------

profile_dirs: typing.Dict[str, Path] = {}
for check_dir in Path(".").glob("*"):
    if not check_dir.is_dir():
        continue

    for profile_dir in check_dir.glob("*"):
        if not profile_dir.is_dir():
            continue

        profile_yml = profile_dir / "profile.yml"
        if profile_yml.is_file():
            profile_dirs[profile_dir.name] = profile_dir

# -----------------------------------------------------------------------------


@app.route("/<path:path>")
async def download_raw(path: str) -> Response:
    components = path.split("/")
    profile = components[0]
    artifact = "/".join(components[3:])

    profile_dir = profile_dirs.get(profile)
    assert profile_dir, f"Missing directory for {profile}"

    return await send_from_directory(profile_dir, artifact)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0")
