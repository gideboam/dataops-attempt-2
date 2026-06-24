from generate import generate_data

def test_generate_100_records():
    data = generate_data(100)

    assert len(data) == 100

def test_record_structure():
    data = generate_data(1)

    record = data[0]

    assert "device_id" in record
    assert "temperature" in record
    assert "humidity" in record
    assert "timestamp" in record
