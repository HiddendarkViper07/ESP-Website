import gspread


def write_sheet(
    spreadsheet: gspread.Spreadsheet,
    title: str,
    rows: list[list],
) -> None:
    """
    Write *rows* (including header) to a worksheet named *title*,
    creating it if it doesn't exist.
    """
    try:
        ws = spreadsheet.worksheet(title)
    except gspread.exceptions.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(
            title=title,
            rows=len(rows),
            cols=len(rows[0])
        )

    ws.clear()
    ws.update(rows, value_input_option="USER_ENTERED")

    # Bold the header row only if there are data rows
    if len(rows) > 1:
        ws.format("1", {"textFormat": {"bold": True}})

    print(f"  ✓ '{title}' – {len(rows) - 1} data rows written")
