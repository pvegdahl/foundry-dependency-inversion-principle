import os
import shutil


def file_sync(source_dir: str, target_dir: str) -> None:
    # (_, _, target_files) = next(os.walk(target_dir))
    # for file in target_files:
    #     os.remove(os.path.join(target_dir, file))

    (_, _, source_files) = next(os.walk(source_dir))
    for file in source_files:
        shutil.copy(src=os.path.join(source_dir, file), dst=os.path.join(target_dir, file))


