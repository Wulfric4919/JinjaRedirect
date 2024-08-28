export type CursorEffectResult = {
    destroy(): void;
}

type DefaultOptions = {
    readonly element?: HTMLElement;
}

export type TrailingCursorOptions = {
    readonly particles?: number;
    readonly rate?: number;
    readonly baseImageSrc?: number;
} & DefaultOptions;

export function trailingCursor(options?: TrailingCursorOptions): CursorEffectResult;
