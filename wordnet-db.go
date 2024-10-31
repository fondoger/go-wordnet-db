package gowordnetdb

import "embed"

//go:embed wordnet-2023/*
var WordnetDataFS embed.FS
