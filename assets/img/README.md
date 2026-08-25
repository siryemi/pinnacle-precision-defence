# Imagery

The site currently ships with **no photography**. Illustrations are inline SVG diagrams and CSS
gradients, so there are no broken-image placeholders and no licensing exposure.

`favicon.svg` is the only asset here.

## If photography is added

Where it would go, in priority order:

1. **Homepage hero** — replace the gradient in `.hero__bg` (`assets/css/site.css`) with a
   `background-image`, keeping the existing dark overlay so the headline stays legible. Test
   contrast after the change.
2. **Rotator panels** — the six `.rotator__figure` blocks in `index.html` currently hold SVG
   diagrams. Photography works here, but the diagrams are arguably stronger for an advisory
   firm: they show a method rather than a stock image of soldiers.
3. **Leadership portraits** — `about/leadership.html`. Consistent framing, plain background.
4. **Sector page headers** — optional.

## Constraints specific to defence photography

- **Licensing.** Do not use stock imagery of foreign forces to illustrate Nigerian capability;
  informed viewers spot it immediately and it undermines the whole site. If real Nigerian
  military photography is used, obtain written permission from the originating authority.
- **OPSEC.** Any photograph taken during an engagement requires clearance from the client's
  security authority before publication. Check for unit identifiers, serial numbers,
  recognisable locations, screens, whiteboards and documents in frame.
- **Personnel consent.** Identifiable serving personnel require individual consent plus their
  chain of command's approval.
- **No implied endorsement.** A photograph of a client's equipment or personnel implies a
  relationship. Do not publish one without the written permission covered in
  `CONTENT-TODO.md` §4.

## Technical notes

- Export at 2× the display size, then compress; AVIF or WebP with a JPEG fallback.
- Hero images should sit under ~250 KB after compression — much of the target audience is on
  mobile data.
- Add `loading="lazy"` to everything below the fold; do **not** lazy-load the hero.
- Every image needs meaningful `alt` text, or `alt=""` if purely decorative.
