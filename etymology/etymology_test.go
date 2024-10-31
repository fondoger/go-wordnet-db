package etymology

import (
	"testing"
)

func TestEtymology(t *testing.T) {
	if Etymology["correctly"] != "03"+"correct" {
		t.Error("Expected 03correct, got", Etymology["correctly"])
	}

}
