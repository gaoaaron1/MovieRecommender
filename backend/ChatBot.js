const { Configuration, OpenAIApi } = require("openai");
require("dotenv").config();

const askToChatGpt = async function (req, res) {
  /**
   * 1. Create/configure OpenAI Instance
   */
  const openAIInstance = _createOpenAIInstance();

  /**
   * 2. Let's talk to chatGPT
   */
  await openAIInstance
    .createCompletion({
      model: "text-davinci-003",
      prompt: req.body.message,
      temperature: 0,
      max_tokens: 500,
    })
    .then((response) => {
      const repliedMessage = response.data.choices[0].text;
      res.send({ from: "chatGpt", data: repliedMessage });
    })
    .catch((error) => {
      // Report error
      console.log("Error ", error);
      res.status(500).send({ error: "Error in communication with ChatGPT" });
    });
};

const _createOpenAIInstance = () => {
  const configuration = new Configuration({
    apiKey: process.env.CHATGPT_TOKEN,
  });
  return new OpenAIApi(configuration);
};

module.exports = {
  askToChatGpt,
};
