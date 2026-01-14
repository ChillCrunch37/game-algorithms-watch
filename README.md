“Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it” [Kernighan].

An algorithm is a sequence of discrete actions that when followed, will result in achieving some goal or solving some problem. In the field of computer science, an algorithm is any well-defined sequence of actions that takes a set of values as input and produces some set of values as output. In other words, an algorithm is a sequence of computational actions that transform the input into the desired output.

# game-algorithms-watch

Daily GitHub alerts and curated learning resources for game algorithms. This project automatically creates issues for new or high-quality repositories related to game algorithms so contributors and learners get GitHub notifications, and it curates examples, exercises, and learning paths to help you study and apply those algorithms.

Short mission (one-liner)
- Empower developers and learners to discover, understand, and apply game algorithms by surfacing high-quality repositories and pairing them with curated explanations, exercises, and sample projects.

Expanded mission (2–3 sentences)
- Monitor the GitHub ecosystem for well-crafted repositories that demonstrate game algorithm techniques (pathfinding, AI, flocking, procedural generation, physics, etc.), and create issues so the community can review, tag, and curate them. Use those discoveries as the basis for learning paths, runnable examples, and small projects that reinforce both theoretical understanding and practical application.

Table of contents
- What this repo does
- Mission & goals
- Pseudocode Expectations 
- How alerts / issues work
- Learning roadmap (topics & suggested projects)
- How to contribute
- Repository structure
- Suggested next steps / admin tasks
- Resources & reading

What this repo does
- Watches for repositories, projects, and examples that implement game-focused algorithms.
- Creates issues for newly discovered, high-quality repositories so maintainers and learners receive notifications.
- Curates selected repos into learning modules with explanations, runnable samples, and exercises.

How alerts / issues work (brief)
- A scheduled process runs daily searches for keywords, tags, and patterns (pathfinding, A*, steering, flocking, behavior-tree, MCTS, procedural generation, etc.).
- When a candidate repo meets quality heuristics (README clarity, example code, tests, license), the bot opens a new issue summarizing the repo and proposing tags and learning placements.
- Community members triage those issues (tag, add to learning modules, or close if irrelevant).

Learning roadmap (topics & sample projects)
- Fundamentals
  - Algorithms & data structures review (graphs, queues, spatial indexes)
  - Suggested mini-project: grid-based pathfinding visualizer
- Pathfinding
  - A*, Dijkstra, Jump Point Search
  - Project: navmesh generator + agent steering between goals
- Steering & Movement
  - Seek, Flee, Arrive, Wander, Obstacle avoidance
  - Project: steering demo with multiple agent behaviors
- Group behaviors
  - Flocking (Boids), formations
  - Project: parameterized flocking playground
- Decision-making & AI
  - Finite State Machines, Behavior Trees, Utility AI, MCTS
  - Project: small AI for a simple game (enemy behaviors, tactical decisions)
- Procedural content
  - Noise functions, dungeon generation, L-systems
  - Project: procedural level generator + walkthrough
- Optimization & performance
  - Spatial partitioning (quad/octrees), data-oriented design
  - Project: performance comparison of collision detection methods
- Networking & determinism (advanced)
  - Deterministic lockstep, snapshot interpolation
  - Project: 2-player deterministic simulation demo

How to contribute
- Found a repo that matches the mission? Submit it via Issues -> New discovery and include:
  - URL, short summary, why it’s high-quality / educational, suggested tags (topic, language, difficulty)
- Want to help curate? Triage discovery issues: add tags, link to modules, or mark as out-of-scope
- Want to teach? Add a module (folder) with explanation, code samples, and exercises; open a PR to propose it.
- See CONTRIBUTING.md for templates and standards (suggested next step: add this file).

Recommended repository structure
- /discoveries/ — auto-created issues metadata or exported lists
- /modules/
  - /pathfinding/ — explanation, runnable demos, exercises, references
  - /steering/
- /examples/ — minimal demos with readme and run instructions
- /exercises/ — unit-test based challenges to practice implementations
- /tools/ — scripts for the watcher / alerting logic

Suggested README additions & badges
- Add badges for CI, license, issues, and community-contributed modules.
- Add a short “getting started” to explain how to trigger alerts, opt out, or submit items.

Labels & templates (admin suggestions)
- Add labels: discovery, triage-needed, module-proposed, out-of-scope, beginner-friendly, intermediate, advanced, language:python, language:cpp, etc.
- Add issue templates:
  - Discovery submission template (URL, summary, tags)
  - Module proposal template (learning goals, required knowledge, sample project)
- Add a CONTRIBUTING.md and CODE_OF_CONDUCT.md
- Pseudocode Template and guidelines

Sample "learning module" README pattern (brief)
- Goal: what learners will know/do
- Background: short theory
- Example: link to code and runnable demo
- Exercises: 2–4 practice tasks with acceptance tests or expected outputs
- Further reading: links and papers

Resources & reading (suggested links to include)
- A* algorithm resources
- Steering behaviors (Craig Reynolds)
- Behavior Trees & Utility AI references
- Procedural content generation resources
- Papers & tutorials for spatial structures and optimization

Next actionable steps I recommend
1. Replace the current README with this draft (or a trimmed variant).
2. Add basic repo plumbing: CONTRIBUTING.md, ISSUE_TEMPLATEs, labels listed above, and CODE_OF_CONDUCT.md.
3. Create one or two starter modules (e.g., pathfinding and steering) with an example and one exercise each.
4. Consider adding CI for examples (e.g., run demos/tests in GitHub Actions) and a small "discovery watcher" script if not already present.

Contact / maintainers
- If you want, I can:
  - Produce ready-to-commit files for CONTRIBUTING.md and issue templates
  - Draft the first learning module (pathfinding) with runnable example + tests
  - Propose label set and a GitHub Actions workflow to run the watcher
