## Getting Up and Running

To develop Stinky, you'll need Git, Node, and npm (node package manager) installed on your machine. A quick Google should provide you with easy installation downloads for your operating system.

- Git is used for source control via [this repo](https://github.com/cs7290/stinky).
- Node is needed to run the npm environment.
- npm is used to manage JavaScript packages, as well as to run commands such as the SCSS transpiler.

### Installing NPM Packages

Once you have the above tools installed, in the /docs directory run:

```bash
npm install
```

This will install the npm modules into a folder called `node_modules`. It usually takes a while, and will probably throw some warnings, but hopefully no actual errors. This covers third-party framework stuff like bootstrap. Note that `node_modules` is not checked into source control. The modules are only used during development, and aren't needed for the page to actually run.

## Testing

From the root directory run:

```bash
python -m http.server
```

Or with Node.js installed, run:

```bash
npm start
```

Note: this is not strictly necessary, as Stinky as currently written runs from a flat HTML page. You should be able to run it by simply opening `docs/index.html` in your browser, and refreshing whenever you make changes.

## Build SCSS using SASS

Make sure you have installed all dependencies with `npm install`, then run one of the following:

```bash
npm run sass-dev # compiles uncompressed css. This will also start an automatic build process that recompiles the css every time you save a change. All you need to do is reload the page in your browser!
npm run sass-prod # compiles compressed (i.e. "minified") css
```

Either of the commands above will regenerate `css/custom.css`. This will contain all of Bootstrap with any variable overrides or additional classes added from the `scss/custom.scss` file. This is definitely overkill for our application, but was an opportunity to test out the process for customizing Bootstrap.

Note that unlike in many production applications, `css/custom.css` is checked in to source control, and must be included in your commits if it changes. (This also means if you change the SCSS, you should be sure to run one of the sass commands above before your final commit.) This is because there's no build process for the GitHub page that delivers Stinky--it just serves up the HTML page as-is. Thus it needs the final, compiled CSS file, all set and ready to go. Best practice would probably be to run the sass-prod command as your last step before a commit that will be merged into the main branch and go live, but this makes merging and troubleshooting difficult in case of problems.

## Helpful References
- [Importing Bootstrap and using SCSS](https://getbootstrap.com/docs/5.2/customize/sass/)
- [Bootstrap Class Cheatsheet](https://bootstrap-cheatsheet.themeselection.com/)
- [Bootstrap Docs for `navbar` class](https://getbootstrap.com/docs/5.2/components/navbar/#css). Note that we are using a "sticky" navbar, not a "fixed" navbar.