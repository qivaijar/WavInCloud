import pytest

from back_end.database.db_models import AudioData
from back_end.database.db_utils import get_current_datetime


@pytest.fixture(scope="session")
def single_audio_data():
    return AudioData(
        title="Overdose",
        artist="なとり",
        file_path="/some/random/path_1",
        added_at=get_current_datetime(),
    )


@pytest.fixture(scope="session")
def multiple_audio_data():
    audio_data1 = AudioData(
        title="マーシャル・マキシマイザー",
        artist="KAFU",
        file_path="/some/random/path_multi_1",
        genre="Vocaloid utaite|J-Pop",
        added_at=get_current_datetime(),
    )

    audio_data2 = AudioData(
        title="Pretender",
        artist="Official Hige Dandism",
        file_path="/some/random/path_multi_2",
        genre="J-Pop",
        lyric="random lyric blablabla",
        added_at=get_current_datetime(),
    )

    audio_data3 = AudioData(
        title="サインはB",
        alternative_title="Sign wa B",
        artist="B-Komachi",
        file_path="/some/random/path_multi_3",
        lyric="another random lyric blablabla",
        added_at=get_current_datetime(),
    )

    list_audio_data = [audio_data1, audio_data2, audio_data3]

    return list_audio_data
