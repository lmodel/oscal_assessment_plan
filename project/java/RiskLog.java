package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A log of all risk-related tasks taken.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskLog  {

  private List<RiskLogEntry> entries;

}