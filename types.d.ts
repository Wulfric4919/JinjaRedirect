export type TrailingCursorOptions = {
    readonly particles?: number;
    readonly rate?: number;
    readonly baseImageSrc?: number;
} & DefaultOptions;

export function trailingCursor(options?: TrailingCursorOptions): CursorEffectResult;
