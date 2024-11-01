package coca60000

import "testing"

func TestCoca(t *testing.T) {
	println(Coca60000Stripped["the"])
	if Coca60000Stripped["the"] != 1 {
		t.Error("Expected 1, got", Coca60000Stripped["the"])
	}
}
