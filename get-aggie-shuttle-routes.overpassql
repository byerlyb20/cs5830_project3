[out:json][timeout:60];

// 1. Find all bus route relations belonging to the Aggie Shuttle network
relation
  ["type"="route"]
  ["route"="bus"]
  ["network"="Aggie Shuttle"];

// 2. Recurse down to member ways belonging to those relations
way(r);

// 3. Output the way elements along with their node geometry
out body geom;