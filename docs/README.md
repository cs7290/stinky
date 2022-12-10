## Testing

From the root directory run:

```bash
python -m http.server
```

Or with Node.js installed, run:

```bash
npm start
```

## Build SCSS using SASS

Make sure you have installed all dependencies with `npm install`. Then run on of the following:

```bash
npm run sass-dev # compiles uncompressed css
npm run sass-prod # compiles compressed (i.e. "minified") css
```

Either of the commands above will regenerate `css/custom.css`. This will contain all of Bootstrap with any variable overrides or additional classes added from the `scss/custom.scss` file. This is definitely overkill for our application, but was an opportunity to test out the process for customizing Bootstrap.

## Helpful References
- [Importing Bootstrap and using SCSS](https://getbootstrap.com/docs/5.2/customize/sass/)
- [Bootstrap Class Cheatsheet](https://bootstrap-cheatsheet.themeselection.com/)
- [Bootstrap Docs for `navbar` class](https://getbootstrap.com/docs/5.2/components/navbar/#css). Note that we are using a "sticky" navbar, not a "fixed" navbar.