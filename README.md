<p>
  <h1 align="center">TEXEC</h1>
</p>

# Intro

The world 'TEXEC' stands for 'The Executor of the jobs.' **It's a platform-free CI/CD tool** configurable with YAML, like GitHub action.

# Basic Concept

## Why TEXEC?

Text configurable CI tools are the best. GUI CI/CD tools like [jenkins](https://www.jenkins.io/) or [spinnaker](https://spinnaker.io/) offer great GUI, but sometimes they're too hassle and difficult to set up. They have too many options to understand. I got tired of browsing between so many tabs and menus.

GitHub action is one of the best options for CI/CD, but it's only available on GitHub repositories. I want my CI/CD workflow definitions to be platform-free.

TEXEC is a platform-free CI/CD tool inspired by GitHub Action. Its role is to execute jobs as described in the YAML file. What's so special about TEXEC is, you can set the environment of the jobs to be executed. You can choose one of local or Docker Container.

By using TEXEC, you can configure the CI/CD workflow regardless of the platform you use. Let's get started with the following command.

```sh
texec run
```
