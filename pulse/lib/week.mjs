// IST-aware date + ISO-week helpers. ISO 8601: weeks start Monday; week 1 is the week containing the
// year's first Thursday. We label weeks by the ISO week of their IST calendar date.
const IST = 5.5 * 3600 * 1000;
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

// Shift an instant so UTC getters read the IST wall-clock date/time.
export const istShift = (ms) => new Date((typeof ms === 'number' ? ms : new Date(ms).getTime()) + IST);

export const istMonDay = (ms) => { const d = istShift(ms); return `${MON[d.getUTCMonth()]} ${d.getUTCDate()}`; };

export const istHM = (ms) => { const d = istShift(ms); return `${String(d.getUTCHours()).padStart(2, '0')}:${String(d.getUTCMinutes()).padStart(2, '0')}`; };

export function isoWeekLabel(ms) {
  const d = istShift(ms);
  const date = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()));
  const day = (date.getUTCDay() + 6) % 7;           // Mon=0
  date.setUTCDate(date.getUTCDate() - day + 3);      // Thursday of this week decides the ISO year
  const year = date.getUTCFullYear();
  const firstThu = new Date(Date.UTC(year, 0, 4));
  const ftDay = (firstThu.getUTCDay() + 6) % 7;
  firstThu.setUTCDate(firstThu.getUTCDate() - ftDay + 3);
  const week = 1 + Math.round((date - firstThu) / (7 * 864e5));
  return `${year}-W${String(week).padStart(2, '0')}`;
}
