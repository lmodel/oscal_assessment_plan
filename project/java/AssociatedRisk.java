package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Relates the finding to a set of referenced risks.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssociatedRisk  {

  private String risk-uuid;
  private String remarks;

}