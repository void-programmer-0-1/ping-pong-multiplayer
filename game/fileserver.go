package main

import (
	"html/template"
	"net/http"
	"log"
)

func homeRoute(w http.ResponseWriter, r* http.Request){
	tmpl := template.Must(template.ParseFiles("game/index.html"))
	err := tmpl.Execute(w, nil)
	if err != nil{
		http.Error(w, "Failed to render template", http.StatusInternalServerError)
		log.Println("Template execution error:", err)
		return
	}
}

func gameRoute(w http.ResponseWriter, r* http.Request){
	tmpl := template.Must(template.ParseFiles("game/game.html"))
	err := tmpl.Execute(w, nil)
	if err != nil{
		http.Error(w, "Failed to render template", http.StatusInternalServerError)
		log.Println("Template execution error:", err)
		return
	}
}

func aboutRoute(w http.ResponseWriter, r* http.Request){
	tmpl := template.Must(template.ParseFiles("game/about.html"))
	err := tmpl.Execute(w, nil)
	if err != nil{
		http.Error(w, "Failed to render template", http.StatusInternalServerError)
		log.Println("Template execution error:", err)
		return
	}
}



func main() {

	http.Handle("/game/", http.StripPrefix("/game/", http.FileServer(http.Dir("./game"))))
	http.HandleFunc("/", homeRoute)
	http.HandleFunc("/about", aboutRoute)
	http.HandleFunc("/pong-game", gameRoute)

	log.Println("Server started at http://localhost:8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal(err)
	}

}
