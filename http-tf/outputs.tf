# produces an output value named "space_heroes"
output "Infernape_abilities" {
  description = "API that names infernapes abilities"
  value       = data.http.ability.response_body
}

# produces legal JSON output value named "infernape_abilities_json"
output "infernape_abilities_json" {
  description = "API that names infernapes abilities"
  value       = jsondecode(data.http.ability.response_body).abilities    // note the jsondecode()
}    
