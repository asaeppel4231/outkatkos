# outkatkos

Outkatkos is a simple *server outage reporting* system written in Python.

## More numbers

- ***Lines of code**: 194 (Python)
- ***Complexity***: 33 (Python)
- ***LOC*** / ***Complexity***: 5,878787879 (Python)

## TOC

- [*License*](#license)
- [*Name meaning*](#name-meaning)
- [*Editor notice*](#editor-notice)
- [*Native executable download*](#native-executable-download)
- [*Example*](#example)

## License

This project is licensed under the **MIT license**.

See [LICENSE.md](LICENSE.md)

## Name meaning

The name **"outkatkos"** derives from the *first 3 words of the englisch translation of "Ausfall"* (**outage**) and the *finish word of "Ausfall"* (**katkos**).
***Combined*** it means *"undo the outage"*. Of course, **outkatkos** can not *make undo your server outage*, but I think the ***name is good***.

## Editor notice

This project was written in assistance with **AI** and **I used the Helix editor in combination with the *pyrefly* python language server**.

## Native executable download

People who don't like to install the python interpreter can also download the native executable of the current version (v1.0).
The basic release URL on github for that version is [https://github.com/asaeppel4231/outkatkos/releases/tag/v1.0](https://github.com/asaeppel4231/outkatkos/releases/tag/v1.0).
You can download the native executables directly with the following links depending on your operating system:

- Linux: [https://github.com/asaeppel4231/outkatkos/releases/download/v1.0/outkatkos-linux](https://github.com/asaeppel4231/outkatkos/releases/download/v1.0/outkatkos-linux) (native x86_64 ELF binary)
- Windows: [https://github.com/asaeppel4231/outkatkos/releases/download/v1.0/outkatkos-windows.exe](https://github.com/asaeppel4231/outkatkos/releases/download/v1.0/outkatkos-windows.exe) (native x86_64 EXE file)
- macOS: [https://github.com/asaeppel4231/outkatkos/releases/download/v1.0/outkatkos-macos](https://github.com/asaeppel4231/outkatkos/releases/download/v1.0/outkatkos-macos) (native arm64 Mach-O Binary)

## Example

The following example requires an installation of *python 3*. If you don't have one, please download python at [python.org](https://python.org)
```sh
python3 outkatkos.py --ds DATE_START --de DATE_END --ts TIME_START --te TIME_END --server github.com --sender Person
```
An example configuration that you can edit for your purposes is located at [config.example.json](config.example.json)

