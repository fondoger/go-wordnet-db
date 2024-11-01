package etymology

import (
	"testing"
)

func TestEtymology(t *testing.T) {
	if EtymologyStripped["correctly"] != "03"+"correct" {
		t.Error("Expected 03correct, got", EtymologyStripped["correctly"])
	}

}
