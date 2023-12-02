<template>
    <div>
        <h2>Vue.js and D3 Line Chart</h2>
        <svg></svg>
    </div>
</template>

<script lang="ts">
import * as d3 from 'd3'
import { onMounted } from 'vue'

export default {
    setup() {
        const data = {
            edges: [
                {
                    weight: 0.8,
                    source: 'Gioia',
                    target: 'VRACOOP'
                },
                {
                    weight: 0.3,
                    source: 'Gioia',
                    target: 'ERRO ETXEA'
                },
                {
                    weight: 0.5,
                    source: 'VRACOOP',
                    target: 'ERRO ETXEA'
                }
            ],
            nodes: [
                {
                    Longitude: '-1.0634024',
                    'Quels sont tes besoins actuels ?': 'Creation site internet\nCollecte de fond',
                    "Domaine d'activité": 'Alimentation',
                    'Code postal + ville': 'Bergouey viellenave 64270',
                    'Lieu du projet': 'Bergouey viellenave',
                    Coproduits: 'Déchet compostable en majeur partie',
                    'Nom du Projet': 'Gioia',
                    'Description du projet':
                        'Creation d’un fournil avec son propre moulin, production locale de boulangerie et patisserie en bio suivant les saisons, et pain au levain.',
                    Latitude: '43.4258339',
                    inapp: true,
                    'Maturité du projet': '4 - Fruit (La commercialisation)',
                    "ODD fixé par l'ONU": '3-Bonne santé et bien-être',
                    'Code postal': 64270,
                    'Matières entrantes': 'Produit locaux matière premiere alimentaire',
                    Logo: 'https://v5.airtableusercontent.com/v2/22/22/1700164800000/T4VeC2A6_KUeVajljCh9ig/4y_c7doJTtbUwMsNPtmgylHSnicopXre0RdrNnf5dcFJ1waDfnc5tPwo2yQgiYGKRDzjQg0fMC8TMQ98iHM1paK0WsVyPt8dL9BFM46xvHQDDt4WEv06lUVqcOGLT-H9EkakFUm6i8Rr6ghlXEfGGIHBZl_zEZAdd5V28Vz-WfEVVaWtY_blemQBB3yppPRr/Tc_OlhH1A-vOYAx0r9gWaW31DKfjoStEdUzqikq8w0E'
                },
                {
                    Longitude: '-1.663055',
                    "Domaine d'activité": 'Alimentation,Déchets',
                    'Circularité projet': 'Collecte & Compost',
                    'Code postal + ville': 'Saint Jean de Luz 64500',
                    'Lieu du projet': 'Saint Jean de Luz',
                    Coproduits: 'Palettes, cartons',
                    'Photos du projet':
                        'https://v5.airtableusercontent.com/v2/22/22/1700164800000/jfKgwK_CToVy-5wNIE56lg/f797dOcCfykZf11JIHaGyJ6TksCKhJw8iETq3rnclbyeDCJGYJCUbElWKOR0b09TvH_O5p79hLPFBNy90cwN5K3deRepQgj_pChO5RDWWLMv7oTbinN6xv4WbjE9NzqgILGsFRsdOwFz6iFzDBL6x0ZICuKYlI9aBfqDO7ba86U/Jx28HwdZ_6HfajbwqMb6a_jptqJDxuW9X-fbec8qjJw',
                    'Nom du Projet': 'VRACOOP',
                    'Description du projet':
                        "Vracoop développe des solutions pour faciliter la vente de produits en vrac dans les commerces et ainsi diminuer les déchets d'emballages. \n\nDes épiceries vrac sont équipées d'un système d'encaissement spécialisé, permettant aux consommateurs de rapporter leurs propres contenants et de déduire automatiquement leurs poids au moment du passage en caisse. \n\nAussi le silo distributeur Vracoop et le bac sont éco-conçus et fabriqués localement, ils sont à la fois économiques et réduits en plastique pour que chaque commerçant puisse mettre en place aisément son rayon vrac. \n\nEnfin, l'application web maYam apporte information utile et traçabilité pour rendre le vrac encore plus transparent et le rendre aussi irréprochable que le pré-emballé.",
                    Latitude: '43.388051',
                    inapp: true,
                    'Maturité du projet': "1 - Graine (L'idée)",
                    "ODD fixé par l'ONU":
                        '3-Bonne santé et bien-être,11-Villes et communautés durable,12-Consommation et production responsables',
                    'Code postal': 64500,
                    'Matières entrantes': 'Bois',
                    'Site internet': 'http://vracoop.fr',
                    Logo: 'https://v5.airtableusercontent.com/v2/22/22/1700164800000/g1lUPkAoqbv5ByqSWB4IOw/b3piCfLmET_hO6ojNIRHv-d2OAOXbOjYSKgMuwOwTn7gMvO0RPMJTbh0fjQSBAjOYxRWmkKyub9eqs2QtHbzTwkX9lEDasYijOwSMQJ_fNMulkQecI6ondRnC1eWUn5AebgD1RZ3fiHuX-ze3HvTg6MbEcZJNioQUNLzLRWJQYwyhjVp7p683BzIMPiX9py3/PP8kDYNKqtY5cbdWqCHDbgXapOID8w0hG3vtdUZmM1g'
                },
                {
                    Longitude: '-1.134723',
                    'Quels sont tes besoins actuels ?':
                        'Aide pour le plan de financement et Business plan.',
                    "Domaine d'activité": 'Bâtiment,Autre,Energie',
                    'Circularité projet':
                        "L'Echappée Verte,Forêt comestible de Higas,Le Recup'Truck 64,AIMA",
                    'Code postal + ville': 'OREGUE 64120',
                    'Lieu du projet': 'OREGUE',
                    Coproduits: 'Normalement, très très très peu !',
                    'Nom du Projet': 'ERRO ETXEA',
                    'Description du projet':
                        "ERRO ETXEA : Conception et construction d'un habitat durable avec activités de tourisme au Pays Basque.\n-Minimiser l'impact visuel et environnemental dans la construction.-Utiliser des matériaux recyclés et renouvelables disponibles en local (- de 250km).\n-Viser l'auto suffisance énergétique (avec raccord au réseau traditionnel en secours si nécessaire).\n-Maximiser le captage en eaux pluviales disponibles sur le terrain avec utilisation en circuit fermé et traitement biologique pour les équipements (eau domestique, arrosage potager et piscine biologique).\n-Respecter les codes architecturaux du pays baque. Orientation, ouverture, couleurs, colombages, côté est seulement, etc.\n-Proposer des séjours à thèmes en partenariat avec les guides touristiques locaux sur différents thèmes (histoire, mythes, gastronomie, faune et flore endémique).\n\n",
                    Latitude: '43.394478',
                    inapp: true,
                    'Pièce jointe du projet':
                        'https://v5.airtableusercontent.com/v2/22/22/1700164800000/Yl7qIh9BOOj--Yiq49w99A/0dhoMMP6O4HWxfYFUl9ahgIfgL_MLPWiRCWzfQ3U0OLbI3hhrJ7Tf9-DmdewvITNoxGMLUC0tZGcw7iuKZjvkQU2WxiUcQcwRwC5cmo45r_nccDDd_Rg0xsj3SlTW642kTmmn6eGY39GFbjW0lOSCWhJRlnNJLMaDeF7x9GwYxYj6Qv8WggFdLdOaWWwOLd6r38J5XWi4xChJ-gnF-J6JQ/j7NRHMr5mP7LmnpnLv1oQk2a35qFni_ffrY1cL5Vm3c',
                    'Maturité du projet': '2 - Plant (Le business model)',
                    "ODD fixé par l'ONU":
                        "6-Eau propre et assainissement,7-Energie propre et d'un coût abordable,11-Villes et communautés durable,3-Bonne santé et bien-être",
                    'Code postal': 64120,
                    'Matières entrantes':
                        'Projet de construction avec des matières recyclés ou naturelles. Écosystème déjà bien défini avec des entités locales (voir dossier).',
                    Logo: 'https://v5.airtableusercontent.com/v2/22/22/1700164800000/Fa4OiYhzKfX69NqO4rUyVg/HRs5DJFnh8FnHU-5m4jdYfkcnUy6gV7N0GU4SWJWt43k1SZR6yNCL7Xijt1eEzaJyNajQjE6u6sNpn9P2KVmn7rAzsyxShq2pX-XuxyTWbPnfEzua3zrny70DdA_jsKEZoFuEA_yHh0HQZql6fUI8A/WUcqm8l8wSmx1jXlFOBk2upo-eN1NHrGwAZ_UBQPH3M'
                }
            ]
        }

        onMounted(() => {
            // Specify the dimension of the chart
            const width = 800
            const height = 500

            // Specify the color scale
            const color = d3.scaleOrdinal(d3.schemeCategory10)

            // Extract nodes and links from data
            const nodes = data.nodes.map((node: any) => ({
                id: node['Nom du Projet'],
                ...data
            }))
            const links = data.edges

            // Create a force simulation
            const simulation = d3
                .forceSimulation(nodes)
                .force(
                    'link',
                    d3.forceLink(links).id((d: any) => (d as any).id)
                )
                .force('charge', d3.forceManyBody())
                .force('x', d3.forceX())
                .force('y', d3.forceY())

            // Create the SVG container
            const svg = d3
                .select('svg')
                .attr('width', width)
                .attr('height', height)
                .attr('viewBox', [-width / 2, -height / 2, width, height])
                .attr('style', 'max-width: 100%; height: auto;')

            // Add a line for each link, add a circle for each node
            const link = svg
                .append('g')
                .attr('stroke', '#999')
                .attr('stroke-opacity', 0.6)
                .selectAll('line')
                .data(links)
                .join('line')
                .attr('stroke-width', (d: any) => Math.sqrt(d.value))

            const node = svg
                .append('g')
                .attr('stroke', '#fff')
                .attr('stroke-width', 1.5)
                .selectAll('circle')
                .data(nodes)
                .join('circle')
                .attr('r', 5)
                .attr('fill', (d: any) => color(d.group))

            node.append('title').text((d: any) => d.id)

            // Add a drag behavior
            node.call(d3.drag().on('start', dragstarted).on('drag', dragged).on('end', dragended))

            // Set the position attributes of links and nodes each time the simulation ticks
            simulation.on('tick', () => {
                link.attr('x1', (d: any) => d.source.x)
                    .attr('y1', (d: any) => d.source.y)
                    .attr('x2', (d: any) => d.target.x)
                    .attr('y2', (d: any) => d.target.y)

                node.attr('cx', (d: any) => d.x).attr('cy', (d: any) => d.y)
            })

            // Reheat the simulation when drag starts, and fix the subject position
            function dragstarted(event: any) {
                if (!event.active) simulation.alphaTarget(0.3).restart()
                event.subject.fx = event.subject.x
                event.subject.fy = event.subject.y
            }

            // Update the subject (dragged node) position during drag
            function dragged(event: any) {
                event.subject.fx = event.x
                event.subject.fy = event.y
            }

            // Restore the target alpha so the simulation cools after dragging ends.
            // Unfix the subject position now that it’s no longer being dragged
            function dragended(event: any) {
                if (!event.active) simulation.alphaTarget(0)
                event.subject.fx = null
                event.subject.fy = null
            }
        })
    }
}
</script>
