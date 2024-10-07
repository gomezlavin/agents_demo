# Week 4 - Project: Agents
Last week, we explored how to implement functions, a powerful feature to enable LLMs to impact the real world via reading/writing to APIs. We saw the impact of prompts in creating consistent behavior, although even greater reliability requires fine-tuning (covered in Week 5).

Functions are great for simple tasks, but insufficient for higher level objectives. Researchers and developers have created the concept of agents to achieve goals that require many steps and error resolution.

Agents are designed with capabilities such as:

Planning - breaking down a goal into many steps
Tool use - calling functions as necessary
Memory - retaining short and long term context
Orchestration - collaborating with other agents to achieve the objective.
There are a number of popular agent frameworks:

LangChain
LangGraph
Microsoft Autogen
CrewAI
In my opinion, those frameworks are overengineered, brittle, and hard to debug. The reality is that the idea of agents is close to the frontier of LLM – currently difficult to make work in production. That said, model capabilities are advancing in leaps and bounds.

Check out Devin: https://www.cognition.ai/blog/introducing-devin, where a research team has demonstrated a sophisticated agent capable of successfully navigating hundreds of steps to solve complex development tasks.

In this lab, we're going to build our own agent framework and develop a primitive version of Devin. We'll explore planning strategies such as ReAct, Self-consistency, and Reflexion.

By the end of this lab, you should have a pretty good idea of what's happening behind the scenes at LangChain, CrewAI, et al.