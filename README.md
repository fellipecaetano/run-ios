This is a script that acts as a companion to `react-native run-ios` by allowing users to select a specific iOS Simulator, by name, before launching the app.

## Installation

There are two suggested options for installation:

### Link the script from your `PATH`

- Clone this repository somewhere in your environment;
- Create a soft link from a directory inside your `PATH` to `run-ios.bin.py`;

### Add this repository as a submodule to your project

- Create a `scripts` or `bin` directory inside your project;
- Add this repository as a submodule inside the directory you just created;
- Create a soft link to `run-ios/bin.py`;

These are just suggestions and admitedly horrible ones, but a canoninal installation method is in the works.

## Usage

Just run `bin.py --simulator <simulator_name>` from the same level as your `package.json` since the script depends on `react-native run-ios`.  `<simulator_name>` is a string formatted as `<device_name> (<os_version>)` (e. g. "iPad Pro (10.5 inch) (11.0)").

## Contributing

Please do! This is very raw and rough around the edges but hopefully we can turn this into a drop-in replacement for the original `run-ios` script. Open as many PRs as you like, however it suits you!
