package etymology

import (
	"testing"
)

func TestEtymology(t *testing.T) {
	if EtymologyStripped["correctly"] != "correct" {
		t.Error("Expected correct, got", EtymologyStripped["correctly"])
	}
	if EtymologyStripped["unhappiness"] != "unhappy" {
		t.Error("Expected unhappy, got", EtymologyStripped["unhappiness"])
	}
	if EtymologyStripped["unhappy"] != "happy" {
		t.Error("Expected happy, got", EtymologyStripped["unhappy"])
	}
}
