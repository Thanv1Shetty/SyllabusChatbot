{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2dbbd0dc-609d-4ced-b44c-af76af401a0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\thasw\\anaconda3\\lib\\site-packages (1.32.0)\n",
      "Requirement already satisfied: requests in c:\\users\\thasw\\anaconda3\\lib\\site-packages (2.32.2)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from requests) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from requests) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from requests) (2024.6.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3c0e90bc-d868-429d-a1db-e70fa475c2de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: ollama in c:\\users\\thasw\\anaconda3\\lib\\site-packages (0.6.1)\n",
      "Requirement already satisfied: httpx>=0.27 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from ollama) (0.28.1)\n",
      "Requirement already satisfied: pydantic>=2.9 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from ollama) (2.12.5)\n",
      "Requirement already satisfied: anyio in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from httpx>=0.27->ollama) (4.2.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from httpx>=0.27->ollama) (2024.6.2)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from httpx>=0.27->ollama) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from httpx>=0.27->ollama) (3.7)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx>=0.27->ollama) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pydantic>=2.9->ollama) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.41.5 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pydantic>=2.9->ollama) (2.41.5)\n",
      "Requirement already satisfied: typing-extensions>=4.14.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pydantic>=2.9->ollama) (4.15.0)\n",
      "Requirement already satisfied: typing-inspection>=0.4.2 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from pydantic>=2.9->ollama) (0.4.2)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\thasw\\anaconda3\\lib\\site-packages (from anyio->httpx>=0.27->ollama) (1.3.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install  ollama"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a8ecddb1-06ea-46da-8389-8e6ba0a3003e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-03-30 20:22:17.493 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\thasw\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "\n",
    "def load_syllabus():\n",
    "    with open(\"syllabus.txt\", \"r\") as f:\n",
    "        return f.read()\n",
    "\n",
    "\n",
    "def create_prompt(question, syllabus):\n",
    "    prompt = f\"\"\"\n",
    "    You are a syllabus FAQ assistant.\n",
    "    Answer only from the syllabus topics below.\n",
    "    If question is outside syllabus, say \"Not in syllabus\".\n",
    "\n",
    "    Syllabus:\n",
    "    {syllabus}\n",
    "\n",
    "    Question:\n",
    "    {question}\n",
    "\n",
    "    Answer:\n",
    "    \"\"\"\n",
    "    return prompt\n",
    "\n",
    "\n",
    "def ask_llm(prompt):\n",
    "    response = requests.post(\n",
    "        \"http://localhost:11434/api/generate\",\n",
    "        json={\n",
    "            \"model\": \"llama3\",\n",
    "            \"prompt\": prompt,\n",
    "            \"stream\": False\n",
    "        }\n",
    "    )\n",
    "    return response.json()[\"response\"]\n",
    "\n",
    "\n",
    "st.title(\" Smart Syllabus FAQ Chatbot\")\n",
    "\n",
    "syllabus = load_syllabus()\n",
    "question = st.text_input(\"Ask a syllabus question:\")\n",
    "\n",
    "if st.button(\"Ask\"):\n",
    "    prompt = create_prompt(question, syllabus)\n",
    "    answer = ask_llm(prompt)\n",
    "    st.write(\"Answer:\", answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82e4f95d-62bb-48c8-82ad-84816126b818",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
