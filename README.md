# Tampa Bay owner-occupied home values by ZCTA, 2020-2024

Richard Cieplechowicz (also known as Ryszard Cieplechowicz) · September 26, 2026

This table looks at the value distribution of owner-occupied homes in 132 ZIP Code Tabulation Areas (ZCTAs) assigned to Hillsborough, Pinellas, Pasco or Hernando County. It is a second cut of the 2020-2024 American Community Survey (ACS) five-year data, distinct from the earlier Tampa Bay rent-burden dataset. It adds the published 90% margin of error for each median and four value bands for owner-occupied units, rather than treating rent and home value as the same market.

## One useful comparison

Across these 132 ZCTAs, the B25075 estimates sum to 902,658 owner-occupied housing units. An estimated 214,053 of those units (23.7%) are in value bands of $500,000 or more. By assigned county, the share is 27.5% in Hillsborough, 27.0% in Pinellas, 15.5% in Pasco and 9.0% in Hernando. Those are aggregate band-count shares for the selected ZCTAs. They are not the median price of a house, a sale-price measure or an estimate for every address in the county.

## Source and method

Source: U.S. Census Bureau, ACS 2020-2024 five-year detailed tables [B25075, Value](https://api.census.gov/data/2024/acs/acs5/groups/B25075.html) and [B25077, Median Value (Dollars)](https://api.census.gov/data/2024/acs/acs5/groups/B25077.html), retrieved from the [Census Reporter API](https://api.censusreporter.org/1.0/data/show/acs2024_5yr?table_ids=B25075,B25077&geo_ids=86000US33511) for release `acs2024_5yr`. The API response reports its release as ACS 2024 5-year, years 2020-2024, and gives the Census estimates and margins of error. Census Reporter is a data access layer, not the data author.

The ZCTA list and four-county assignment carry over from [the prior 132-ZCTA dataset](https://github.com/richard-cieplechowicz/tampa-bay-zip-housing-data): 2020 Census ZCTA-to-county relationship, largest land-area share, and a minimum of 500 residents. A ZCTA crossing county boundaries is counted only under its assigned county. The current CSV was checked row-for-row against the prior CSV's B25077 median: all 132 match where an estimate is available.

For every ZCTA, the four bands sum to B25075's owner-occupied total: below $300k (categories 02-20), $300k-$499,999 (21-22), $500k-$999,999 (23-24), and $1m+ (25-27). The $500k+ percentage is (bands 23-27 / B25075 total) × 100, rounded to one decimal. Empty cells indicate no published usable estimate. Four ZCTAs have fewer than 300 estimated owner-occupied units and are flagged. Three have no usable B25077 median; they still retain B25075 band data where published.

## Columns

- `zcta`: five-digit Census ZIP Code Tabulation Area, not necessarily a USPS ZIP.
- `county`: the assigned county, per the prior dataset's 2020 relationship-file method.
- `population`: ACS B01003 population estimate carried over from the prior dataset for filtering/context, not a housing denominator.
- `owner_occupied_units`: B25075 total, estimate.
- `median_owner_occupied_value_usd`: B25077 estimate in dollars.
- `median_value_moe_90pct_usd`: B25077 ACS 90% margin of error in dollars; do not treat tiny differences between medians as meaningful.
- `owner_units_value_below_300k`, `owner_units_value_300k_to_499k`, `owner_units_value_500k_to_999k`, `owner_units_value_1m_plus`: B25075 estimated unit counts, not transaction counts.
- `owner_share_value_500k_plus_pct`: share of owner-occupied units in the two highest bands.
- `small_owner_sample_flag`: `yes` when estimated owner-occupied units are below 300. This is an analytic caution threshold, not an official Census quality flag.

## Limits

ACS is a survey, not a parcel census. Its 2020-2024 five-year estimates reflect responses over five years, not 2024 transaction prices or current asking prices. B25077 covers only owner-occupied homes and is a self-reported estimated value, not all housing stock. ZCTAs approximate but are not identical to USPS ZIP codes. A ZCTA assigned to one county can extend into another. Margins of error on band-count sums and derived shares were not calculated, so close percentage comparisons should not be overinterpreted. Do not average ZIP medians to claim a metro median. The four-county sums represent only the 132 selected ZCTAs and include sampling uncertainty. Values with small owner populations warrant extra care.

## Reproducibility and license

The companion `build.py` regenerates the CSV from the original public Census Reporter response and the prior dataset's CSV. Source API response and input CSV are included as downloaded snapshots with the release identified. The derived compilation is offered under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); U.S. Census source data are public domain. Cite: Cieplechowicz, Richard (Ryszard). *Tampa Bay owner-occupied home values by ZCTA, 2020-2024* (2026). U.S. Census Bureau, ACS 2020-2024 five-year detailed tables B25075 and B25077.
