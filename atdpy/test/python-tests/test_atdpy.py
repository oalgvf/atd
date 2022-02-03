"""
Test suite for all Python code, some of which is generated by atdpy.

Each function starting with 'test_' is executed as a test by pytest.
"""

import manual_sample
import everything as e


def test_sample():
    a_obj = manual_sample.Root(id="hello", await_=True, items=[[1, 2], [3]])
    a_str = a_obj.to_json_string()

    b_str = '{"id": "hello", "await": true, "items": [[1, 2], [3]]}'
    b_obj = manual_sample.Root.from_json_string(a_str)
    b_str2 = b_obj.to_json_string()

    assert b_str == b_str2  # depends on json formatting (whitespace...)
    assert b_str2 == a_str


def test_sample_missing_field():
    try:
        manual_sample.Root.from_json_string('{}')
        assert False
    except ValueError:
        pass


def test_sample_wrong_type():
    try:
        manual_sample.Root.from_json_string('["hello"]')
        assert False
    except ValueError:
        pass


def test_everything_to_json():
    a_obj = e.Root(
        id="abc",
        await_=True,
        __init__=1.5,
        items=[[], [1, 2]],
        extras=[17, 53],
        answer=42,
        aliased=e.Alias([8, 9, 10]),
        point=(3.3, -77.22),
        kinds=[
            e.Kind(e.WOW()),
            e.Kind(e.Thing(99)),
            e.Kind(e.Amaze(["a", "b"])),
            e.Kind(e.Root_())
        ]
    )
    a_str = a_obj.to_json_string(indent=2)
    print(a_str)

    b_str = \
        """{
  "ID": "abc",
  "await": true,
  "__init__": 1.5,
  "items": [
    [],
    [
      1,
      2
    ]
  ],
  "extras": [
    17,
    53
  ],
  "answer": 42,
  "aliased": [
    8,
    9,
    10
  ],
  "point": [
    3.3,
    -77.22
  ],
  "kinds": [
    "wow",
    [
      "Thing",
      99
    ],
    [
      "!!!",
      [
        "a",
        "b"
      ]
    ],
    "Root"
  ]
}"""
    b_obj = e.Root.from_json_string(a_str)
    b_str2 = b_obj.to_json_string(indent=2)

    assert b_str == b_str2  # depends on json formatting (whitespace...)
    assert b_str2 == a_str


def test_kind():
    x = e.Kind(e.WOW())
    assert x.kind == x.value.kind
    assert x.kind == 'WOW'


# print updated json
test_everything_to_json()
