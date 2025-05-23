from data_management.models import Main, Spec
from django.db.models import Q
from decimal import Decimal

def get_spec_value(code: str, field: str) -> float:
    try:
        spec = Spec.objects.get(productcode=code)
        return float(getattr(spec, field) or 0)
    except Spec.DoesNotExist:
        return 0

def get_ratio(main: Main, index: int) -> tuple:
    ref = getattr(main, f'ref{index}')
    ratio = getattr(main, f'ratio{index}')
    if ref and ratio:
        return ref, float(ratio)
    return None

def calculate_weighted_parameters(tscode: str) -> dict:
    try:
        main = Main.objects.get(code=tscode)
    except Main.DoesNotExist:
        raise ValueError(f"No 'main' record found for code: {tscode}")

    # Gather valid (ref, ratio) pairs
    components = []
    for i in range(1, 7):
        pair = get_ratio(main, i)
        if pair:
            components.append(pair)

    if not components:
        raise ValueError("No valid components found to calculate weighted parameters.")

    # Weighted calculations
    def weighted_avg(field):
        return round(sum(get_spec_value(ref, field) * ratio for ref, ratio in components), 4)

    sg_avg = weighted_avg('sgavg')
    ri_avg = weighted_avg('riavg')
    fp_avg = round(sum(get_spec_value(ref, 'flashpoint') * ratio for ref, ratio in components), 0)

    # Clamp flashpoint max to 100
    fp_avg = min(fp_avg, 100)

    # Add ±0.01 margin range
    margin = 0.01
    sg_range = f"{round(sg_avg - margin, 4)} - {round(sg_avg + margin, 4)}"
    ri_range = f"{round(ri_avg - margin, 4)} - {round(ri_avg + margin, 4)}"

    # Special rule if Ratio1 == 1.0
    if getattr(main, 'ratio1', 0) == 1.0:
        sg_avg = get_spec_value(main.ref1, 'sglow')

    return {
        'sg_avg': sg_avg,
        'sg_range': sg_range,
        'ri_avg': ri_avg,
        'ri_range': ri_range,
        'flash_point': int(fp_avg)
    }
