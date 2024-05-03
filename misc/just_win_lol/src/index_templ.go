// Code generated by templ - DO NOT EDIT.

// templ: version: v0.2.663
package main

//lint:file-ignore SA4006 This context is only used if a nested component is present.

import "github.com/a-h/templ"
import "context"
import "io"
import "bytes"
import "strings"

import (
	"fmt"
	"slices"
)

func cardPos(idx int, num string, suit string) templ.CSSClass {
	var templ_7745c5c3_CSSBuilder strings.Builder
	templ_7745c5c3_CSSBuilder.WriteString(string(templ.SanitizeCSS(`background-position`, fmt.Sprintf("-%dpx -%dpx", slices.Index(cards, num)*142, slices.Index(suits, suit)*190))))
	templ_7745c5c3_CSSID := templ.CSSID(`cardPos`, templ_7745c5c3_CSSBuilder.String())
	return templ.ComponentCSSClass{
		ID:    templ_7745c5c3_CSSID,
		Class: templ.SafeCSS(`.` + templ_7745c5c3_CSSID + `{` + templ_7745c5c3_CSSBuilder.String() + `}`),
	}
}

func indexComponent() templ.Component {
	return templ.ComponentFunc(func(ctx context.Context, templ_7745c5c3_W io.Writer) (templ_7745c5c3_Err error) {
		templ_7745c5c3_Buffer, templ_7745c5c3_IsBuffer := templ_7745c5c3_W.(*bytes.Buffer)
		if !templ_7745c5c3_IsBuffer {
			templ_7745c5c3_Buffer = templ.GetBuffer()
			defer templ.ReleaseBuffer(templ_7745c5c3_Buffer)
		}
		ctx = templ.InitializeContext(ctx)
		templ_7745c5c3_Var1 := templ.GetChildren(ctx)
		if templ_7745c5c3_Var1 == nil {
			templ_7745c5c3_Var1 = templ.NopComponent
		}
		ctx = templ.ClearChildren(ctx)
		_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteString("<!doctype html><html><head><script src=\"https://unpkg.com/htmx.org@1.9.12\" integrity=\"sha384-ujb1lZYygJmzgSwoxRggbCHcjc0rB2XoQrxeTUQyRjrOnlCoYta87iKBWq3EsdM2\" crossorigin=\"anonymous\"></script><link href=\"/static/style.css\" rel=\"stylesheet\"><script src=\"/static/anim.js\"></script><title>just win lol</title></head><body class=\"scanlines\"><div class=\"container\"><div class=\"sidebar-container\"><div class=\"padding-top\"></div><div class=\"blind-name pixel-corners\">The Bigger Mouth</div><div class=\"blind-desc pixel-corners\"><div class=\"blind-desc-text\">Only Flush Five hands will score this round</div><img class=\"blind-icon\" src=\"static/the-mouth.png\"><div class=\"blind-score-info pixel-corners\"><span style=\"font-size: 20px;\">Score at least</span> <span><img src=\"static/chip.png\"> <span style=\"font-size: 46px;color: #ee4a43;\">70,000</span></span> <span style=\"font-size: 20px;\">Reward: <span style=\"color: #e0b35c;\">$$$$$$</span></span></div></div><div class=\"round-score pixel-corners\"><div class=\"round-score-text\">Round score</div><div class=\"round-score-number pixel-corners\"><span><img src=\"static/chip.png\"> 39,958</span></div></div><div class=\"score-info pixel-corners\"><div class=\"hand-info\">????? lvl.?</div><div class=\"hand-chips pixel-corners\">?</div><div class=\"hand-x\">X</div><div class=\"hand-mult pixel-corners\">?</div></div><div class=\"run-info-button pixel-corners\">Run Info</div><div class=\"options-button pixel-corners\">Options</div><div class=\"game-info\"><div class=\"hands pixel-corners\"><div class=\"hands-text\">Hands</div><div class=\"hands-number pixel-corners\">10</div></div><div class=\"discards pixel-corners\"><div class=\"discards-text\">Discards</div><div class=\"discards-number pixel-corners\">0</div></div><div class=\"money pixel-corners\"><div class=\"inner-money pixel-corners\">$0</div></div><div class=\"ante pixel-corners\"><div class=\"ante-text\">Ante</div><div class=\"ante-number pixel-corners\"><span style=\"font-size: 56px;color: #fb8e02;\">7</span><span style=\"font-size: 26px;\">/</span><span style=\"font-size: 36px;\">8</span></div></div><div class=\"round pixel-corners\"><div class=\"round-text\">Round</div><div class=\"round-number pixel-corners\">24</div></div></div><div class=\"padding-bottom\"></div></div><div class=\"jokers-area\"><div class=\"jokers-amount\">0/5</div><div class=\"jokers pixel-corners\"><img class=\"card\" style=\"background-color: transparent; background-image:none;\" src=\"static/turtle-bean.png\"> <img class=\"card\" style=\"background-color: transparent; background-image:none;\" src=\"static/smeared-joker.png\"></div></div><div class=\"consumables-area\"><div class=\"consumables-amount\">0/2</div><div class=\"consumables pixel-corners\"></div></div><div class=\"hand\"></div><div class=\"play-area\"></div><div class=\"buttons\"><button class=\"pixel-corners play-hand-button\" hx-get=\"/hand\" hx-trigger=\"click\" hx-target=\".hand\" hx-swap=\"innerHTML\">Get Hand</button><div class=\"sort-hand-area pixel-corners\"><div class=\"sort-hand-text\">Sort Hand</div><div class=\"sort-hand-rank-button pixel-corners\">Rank</div><div class=\"sort-hand-suit-button pixel-corners\">Suit</div></div><div class=\"discard-hand-button pixel-corners\">Discard</div><div class=\"hand-drawn-amount\">0/0</div></div><div class=\"deck\"><img style=\"padding-left: 10px;padding-bottom:30px;background-color:transparent;background-image:none;\" class=\"card pixel-corners\" src=\"static/card-back.png\"></div></div></body></html>")
		if templ_7745c5c3_Err != nil {
			return templ_7745c5c3_Err
		}
		if !templ_7745c5c3_IsBuffer {
			_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteTo(templ_7745c5c3_W)
		}
		return templ_7745c5c3_Err
	})
}

func handComponent(hand []string) templ.Component {
	return templ.ComponentFunc(func(ctx context.Context, templ_7745c5c3_W io.Writer) (templ_7745c5c3_Err error) {
		templ_7745c5c3_Buffer, templ_7745c5c3_IsBuffer := templ_7745c5c3_W.(*bytes.Buffer)
		if !templ_7745c5c3_IsBuffer {
			templ_7745c5c3_Buffer = templ.GetBuffer()
			defer templ.ReleaseBuffer(templ_7745c5c3_Buffer)
		}
		ctx = templ.InitializeContext(ctx)
		templ_7745c5c3_Var2 := templ.GetChildren(ctx)
		if templ_7745c5c3_Var2 == nil {
			templ_7745c5c3_Var2 = templ.NopComponent
		}
		ctx = templ.ClearChildren(ctx)
		for idx, card := range hand {
			_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteString(" ")
			if templ_7745c5c3_Err != nil {
				return templ_7745c5c3_Err
			}
			var templ_7745c5c3_Var3 = []any{"card", "pixel-corners", cardPos(idx, card, "c")}
			templ_7745c5c3_Err = templ.RenderCSSItems(ctx, templ_7745c5c3_Buffer, templ_7745c5c3_Var3...)
			if templ_7745c5c3_Err != nil {
				return templ_7745c5c3_Err
			}
			_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteString("<div class=\"")
			if templ_7745c5c3_Err != nil {
				return templ_7745c5c3_Err
			}
			var templ_7745c5c3_Var4 string
			templ_7745c5c3_Var4, templ_7745c5c3_Err = templ.JoinStringErrs(templ.CSSClasses(templ_7745c5c3_Var3).String())
			if templ_7745c5c3_Err != nil {
				return templ.Error{Err: templ_7745c5c3_Err, FileName: `index.templ`, Line: 1, Col: 0}
			}
			_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteString(templ.EscapeString(templ_7745c5c3_Var4))
			if templ_7745c5c3_Err != nil {
				return templ_7745c5c3_Err
			}
			_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteString("\"></div>")
			if templ_7745c5c3_Err != nil {
				return templ_7745c5c3_Err
			}
		}
		if !templ_7745c5c3_IsBuffer {
			_, templ_7745c5c3_Err = templ_7745c5c3_Buffer.WriteTo(templ_7745c5c3_W)
		}
		return templ_7745c5c3_Err
	})
}
