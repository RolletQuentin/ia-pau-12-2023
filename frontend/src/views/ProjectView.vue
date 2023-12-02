<template>
    <div>
        <h2>Vue.js and D3 Line Chart</h2>
        <svg></svg>
    </div>
</template>

<script lang="ts">
import * as d3 from 'd3'
import { ref } from 'vue'

export default {
    setup() {
        const data = ref()

        function fetchData() {
            fetch('http://localhost:8000/links-between-projects/')
                .then((response) => response.json())
                .then((responseData) => {
                    data.value = responseData
                    console.log(data)
                    createGraph()
                })
                .catch((error) => console.error(error))
        }
        fetchData()

        function createGraph() {
            // Specify the dimension of the chart
            const width = 1000
            const height = 1000

            // Specify the color scale
            const color = d3.scaleOrdinal(d3.schemeCategory10)

            // Extract nodes and links from data
            const nodes = data.value.nodes.map((node: any) => ({
                id: node['Nom du Projet'],
                ...data
            }))
            // const links = data.value.edges
            const links = [
                {
                    source: 'Gioia',
                    target: 'VRACOOP',
                    value: 0.3
                },
                {
                    source: 'Gioia',
                    target: 'ERRO ETXEA',
                    value: 0.8
                }
            ]

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
                .force('collide', d3.forceCollide(60))

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
                .attr('stroke-opacity', 1)
                .selectAll('line')
                .data(links)
                .join('line')
                .attr('stroke-width', (d: any) => Math.sqrt(d.value))

            const node = svg
                .append('g')
                .attr('stroke', '#fff')
                .attr('stroke-width', 1)
                .selectAll('circle')
                .data(nodes)
                .join('circle')
                .attr('r', 30)
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
        }
    }
}
</script>