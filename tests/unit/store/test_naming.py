import pytest

from logstick import artifact, store


class TestNamingImage:
    @pytest.mark.parametrize(
        "image, expected",
        [
            ("ubuntu:20.04", "ubuntu:20.04"),
            ("nextlinux/nextlinux-engine:latest", "nextlinux+nextlinux-engine:latest"),
            ("something/nested/image:latest", "something+nested+image:latest"),
        ],
    )
    def test_encode_decode(self, image, expected):
        assert expected == store.naming.image.encode(image)
        assert image == store.naming.image.decode(expected)
