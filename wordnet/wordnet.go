package wordnet

import (
	"embed"
	"io/fs"
)

//go:embed wordnet-2023/*
var rawDir embed.FS

// Wordnet2023 is a dataset from Open WordNet
var Wordnet2023FS, _ = fs.Sub(rawDir, "wordnet-2023")

// print all files in the wordnet-2023 directory
func PrintAllFiles() {
	println("All files in the wordnet-2023 directory:")
	_ = fs.WalkDir(Wordnet2023FS, ".", func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		println(path)
		return nil
	})
}
